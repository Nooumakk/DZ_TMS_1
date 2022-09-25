import psutil


class Frequency:
    def get_data(self):# Получение информации о частоте 
        self.frequency_data = {}
        data = psutil.cpu_freq()
        self.frequency_data.update(
                            current_frequency=data.current,
                            min_frequency=data.min, 
                            max_frequency=data.max
                            )
        return self.frequency_data
    
    def __str__(self):# Присвоение объекту возможность напечатать в отформатированном виде
        frequency_template = (
                                "Текущая частота:{current_frequency} Мгц.\n"
                                "Минимальная частота: {min_frequency} Мгц.\n"
                                "Максимальная частота: {max_frequency} Мгц."
                                )
        res = frequency_template.format(**self.frequency_data)
        return res

class Memory:
    def get_data(self):# Получение информации о памяти
        self.res_memory = {}
        data = psutil.disk_usage('/')
        self.res_memory.update(general_memory=float(data.total/(1024**3)),
                                used_memory=float(data.used/(1024**3)),
                                free_memory=float(data.free/(1024**3)),
                                free_space=data.percent
                                )
        return self.res_memory
    
    def __str__(self):# Присвоение объекту возможность напечатать в отформатированном виде
        memory_template = (
                            "Общее количество памяти: {general_memory:.2f} GB.\n"
                            "Cвободное количество памяти: {used_memory:.2f} GB.\n"
                            "Используемое количество памяти {free_memory:.2f} GB. \n"
                            "Количество свободного пространства(в процентах): {free_space}."
                            )
        res = memory_template.format(**self.res_memory)
        return res

class Network:# Получение информации о сети
    def get_data(self):
        self.res_network = {}
        data = psutil.net_io_counters()
        self.res_network.update(
                            sent_bytes=data.bytes_sent,
                            received_bytes=data.bytes_recv,
                            sent_packages=data.packets_sent,
                            received_packages=data.packets_recv,
                            errors_receiving=data.errin,
                            errors_sending=data.errout,
                            dropin_packages=data.dropin,
                            dropout_packages=data.dropout
                            )
        return self.res_network
    
    def __str__(self):# Присвоение объекту возможность напечатать в отформатированном виде
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
            res = network_template.format(**self.res_network)
            return res

class Power:# Получение информации о кол-ве логических ЦП
    def get_data(self):
        self.res_battery ={}
        data = psutil.sensors_battery()
        self.res_battery.update(battery_charge=data.percent)
        return self.res_battery
    
    def __str__(self):# Присвоение объекту возможность напечатать в отформатированном виде
            battery_template = "Количество заряда батареи(в процентах): {battery_charge}."
            res = battery_template.format(**self.res_battery)

            return res

class Proc:# Получение информации о работающих процессах
    def get_data(self):
        # self.proc_list = []
        self.res = []
        proc_template = "|{pid:^40}|{username:^40}|{name:^40}|"# Формат строки для каждого процесса
        hat_template = "|{:^40}|{:^40}|{:^40}|"# Формат строки для шапки таблицы
        tables = "-"*124
        hat = hat_template.format("Номер процесса","Пользователь","Название процесса")
        self.res.append(tables)
        self.res.append(hat)
        self.res.append(tables)
        for proc in psutil.process_iter(['username', 'name', 'pid']):
            # self.proc_list.append(proc_template.format(**proc.info))
            self.res.append(proc_template.format(**proc.info))# Добавление отформатированной информации в результирующий список
        self.res.append(tables)
        return self.res
    
    def __iter__(self):# Присвоение возможности итерирования
        self.cursor = 0# Создание курсора для дальнейшего перебора
        return self
    
    def __next__ (self):# Присвоение возможности итерирования
        if self.cursor < len(self.proc_list):
            try:
                return self.proc_list[self.cursor]
            finally:
                self.cursor += 1
        else:
            raise StopIteration

class Poison:# Получение информации о состоянии батареи
    def get_data(self):
        self.res_poison = []
        self.res_poison.append(psutil.cpu_count(logical=False))
        return self.res_poison
    
    def __str__(self):# Присвоение объекту возможность напечатать в отформатированном виде
            poison_template = "Количество логических ЦП в системе: {0[0]}."
            res = poison_template.format(str(self.res_poison[0]))
            return res

def main(): # Блок запуска всех объектов
    fre = Frequency()
    fre.get_data()
    print(fre)
    mem = Memory()
    mem.get_data()
    print(mem)
    net = Network()
    net.get_data()
    print(net)
    pow = Power()
    pow.get_data()
    print(pow)
    proc = Proc()
    proc.get_data()
    for el in proc.res:# Перебор и печать всех работающих процессов
        print(el)
        

if __name__ == "__main__":# Точка входа
    main()
