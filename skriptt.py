import psutil
import json


def info_dec(name_file): #Получение имени файла
    def _executor(func):
        def executor():
            res = func()
            json.dump(res, open(name_file, "w"), indent=1) # Создание файла .json с присвоением имени
            return res

        return executor

    return _executor


#Текущая, минимальная, максимальная частота ЦП.
@info_dec("frequency_info.json")
def frequency_info():
    res_frequency = {}
    data = psutil.cpu_freq()
    res_frequency.update(
                            current_frequency=data.current,
                            min_frequency=data.min, 
                            max_frequency=data.max
                            )
    return res_frequency


#Получение информации о памяти
@info_dec("memory_info.json")
def memory_info():
    res_memory = {}
    data = psutil.disk_usage('/')
    res_memory.update(general_memory=float(data.total/(1024**3)),
    used_memory=float(data.used/(1024**3)), # Конвертирование памяти
    free_memory=float(data.free/(1024**3)), # Конвертирование памяти
    free_space=data.percent)
    return res_memory


#Получение информации о сети
@info_dec("network_info.json")
def network_info():
    res_network = {}
    data = psutil.net_io_counters()
    res_network.update(
                        sent_bytes=data.bytes_sent,
                        received_bytes=data.bytes_recv,
                        sent_packages=data.packets_sent,
                        received_packages=data.packets_recv,
                        errors_receiving=data.errin,
                        errors_sending=data.errout,
                        dropin_packages=data.dropin,
                        dropout_packages=data.dropout
                        )
    return res_network


#Получение информации о логических ЦП
def poison_info():
    res_poison = []
    res_poison.append(psutil.cpu_count(logical=False))
    return res_poison


#Получение информации о батарее
@info_dec("battery_info.json")
def power_info():
    res_battery ={}
    data = psutil.sensors_battery()
    res_battery.update(battery_charge=data.percent)
    return res_battery


#Получение информации о процессах
@info_dec("proc_info.json")
def proc_info():
    proc_list = []
    for proc in psutil.process_iter(['username', 'name', 'pid']):
        proc_list.append(proc.info)
    return proc_list

    
#Формирование, форматирование и вывод строк
def show(fre=None,mem=None,net=None,poi=None,power=None,procs=None):
    frequency_template = (
    "Текущая:{current_frequency} Мгц.\n"
    "Минимальная: {min_frequency} Мгц.\n"
    "Максимальная: {max_frequency} Мгц."
    )
    memory_template = (
    "Общее количество памяти: {general_memory:.2f} GB.\n"
    "Cвободное количество памяти: {used_memory:.2f} GB.\n"
    "Используемое количество памяти {free_memory:.2f} GB. \n"
    "Количество свободного пространства(в процентах): {free_space}."
    )
    network_template = (
    "Количество отправленных байтов: {sent_bytes}.\n"
    "Количество полученных байтов: {received_bytes}.\n"
    "Количество отправленных пакетов: {sent_packages}.\n"
    "Количество полученных пакетов: {received_packages}.\n"
    "Общее количество ошибок при получении: {errors_receiving}.\n"
    "Общее количество ошибок при отправке: {errors_sending}.\n"
    "Общее количество входящик пакетов, которые были сброшены: {dropin_packages}.\n"
    "Общее количество исходящик пакетов, которые были сброшены: {dropout_packages}."
    )
    battery_template = "Количество заряда батареи(в процентах): {battery_charge}."
    poison_template = "Количество логических ЦП в системе: {0[0]}."
    proc_template = "|{:^40}|{:^40}|{:^40}|"
    number_proc = "Количество работающих процессов {}:"
    dash = "-"*71
    quantity = len(procs)
    tables = "-"*124
    tables_1 = "|{:^40}|{:^40}|{:^40}|"
    print("\tТекущая, минимальная, максимальная частота:")
    print(frequency_template.format(**fre))
    print(dash)
    print("\tОбщие характеристики памяти:")
    print(memory_template.format(**mem))
    print(dash)
    print("\tОбщие характеристики сети:")
    print(network_template.format(**net))
    print(dash)
    print(battery_template.format(**power))
    print(dash)
    print(poison_template.format(poi))
    print(dash)
    print("\tИнформация о работающих процессах:")
    print(number_proc.format(quantity))
    print(tables)
    print(tables_1.format("Номер процесса","Пользователь","Название процесса"))
    print(tables)
    for el in procs: #Обращение к элементам списка, хранящего в себе словари, в которых содержится информация о процессах.
        el_1 = el.get("pid")
        el_2 = el.get("username")
        el_3 = el.get("name")
        print(proc_template.format(el_1, el_2, el_3))
    print(tables)
    
     
#Блок единого входа
def main():
    frequency_data = frequency_info()
    memory_data = memory_info()
    network_data = network_info()
    poison_data = poison_info()
    power_data = power_info()
    proc_data = proc_info()
    show(fre=frequency_data,mem=memory_data,net=network_data,poi=poison_data,power=power_data,procs=proc_data)


#Блок запуска
if __name__ == "__main__":
    main()
