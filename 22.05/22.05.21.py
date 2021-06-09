from enum import Enum


class _PersonTypeEnum(Enum):
    e_type = 'E'
    m_type = 'M'
    gm_type = 'GM'


class _Name:
    def __init__ (self, f_name : str, sec_name : str, l_name : str, ):
        self._f_name = f_name
        self._sec_name = sec_name
        self._l_name = l_name



class _Person:
    def __init__(self, name : _Name,
                 salary: float,
                 account: int):
        self._name = name
        self._salary = salary
        self._account = account

    @property
    def name(self) -> str:
        raise NotImplementedError


class Employee(_Person):
    _type = _PersonTypeEnum.e_type

    @property
    def name(self) -> str:
        return f'{self._name} E'


class Manager(_Person):
    _type = _PersonTypeEnum.m_type

    @property
    def name(self) -> str:
        return f'{self._name} M'

class GeneralManager(_Person):
    _type = _PersonTypeEnum.gm_type

    @property
    def name(self) -> str:
        return f'{self._name} GM'


if __name__ == '__main__':
    print('start')
    e = [
        Employee(name=f'Артём{i} Михайлович Тугарёв', salary=15000. + i, account=1234 + i)
        for i in range(1000)
    ]

   # e.append(Manager(name='Миша Михайлович Ф.', salary=30000, account=9876))
   # e.append(GeneralManager(name='Jason Михайлович', salary=1030000, account=98764))
   # e.append(GeneralManager(name='Jason Михайлович', salary=1130000, account=98766))


    e.append(GeneralManager(name = _Name(f_name = 'Сергей', l_name = 'Сергеевич', sec_name = 'Сергеев'), salary=1130000, account=98766))


    salary = sum(_e._salary for _e in e)

    for _e in e:
        print(f'Привет, {_e.name}. Вот твоя зарплата {_e._salary}')




