import psutil


dash = "{}".format("-"*70)
def periodicity():
#Текущая, минимальная, максимальная частота ЦП.
    print(dash)
    print("\tТекущая, минимальная, максимальная частота: ")
    frequency = psutil.cpu_freq()
    str_1 = "Текущая:{0[0]:>7} Мгц.\nМинимальная: {0[1]:} Мгц.\nМаксимальная: {0[2]} Мгц.".format(frequency)
    print(str_1)
periodicity()


def memory():
#Память
    usage = psutil.disk_usage('/')
    usage_1 = []
    for el in usage:
        if el > 100:
            res =el/1024**3
            usage_1.append(res)
        else:
            usage_1.append(el)

    str_1 = "Общее количество памяти: {0[0]:.2f}GB.\nСвободное количество памяти: \
{0[1]:.2f}GB.\nИспользуемое количество памяти: \
{0[2]:.2f}GB.\nКоличество занятого пространства(в процентах): \
{0[3]}.".format(usage_1)
    print(dash)
    print("\tОбщая характеристика памяти:")
    print(str_1)
memory()


def info_network():
    network = psutil.net_io_counters()
    str_1 = "Количество отправленных байтов: {0[0]}.\n\
Количество полученных байтов: {0[1]}.\n\
Количество отправленных пакетов: {0[2]}.\n\
Количество полученных пакетов: {0[3]}.\n\
Общее количество ошибок при получении: {0[4]}.\n\
Общее количество ошибок при отправке: {0[5]}.\n\
Общее количество входящик пакетов, которые были сброшены: {0[6]}.\n\
Общее количество исходящик пакетов, которые были сброшены: {0[7]}.".format(network)
    print(dash)
    print("\tХарактеристика загруженности сети:")
    print(str_1)
info_network()


def poison():
    str_1 = "Количество логических ЦП в системе: {}.".format(psutil.cpu_count(logical=False))
    print(dash)
    print(str_1)
    print(dash)
poison()


def power():
    battery = psutil.sensors_battery()
    str_1 = "Количество заряда батареи(в процентах): {}.".format(battery[0])
    print(str_1)
    print(dash)
power()




