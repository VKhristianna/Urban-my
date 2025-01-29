""" Домашнее задание по теме "Асинхронность на практике" """
# Примечания:
# Для обозначения асинхронной функции используйте оператор async.
# Для постановки задачи в режим ожидания используйте оператор await.
# Для задержки в асинхронной функции используйте функцию sleep из пакета asyncio.
# Для запуска асинхронной функции используйте функцию run из пакета asyncio.

import asyncio


async def start_strongman(name, power):
    balls = 5
    print(f'Силач {name} начал соревнования.')
    for i in range(1, balls + 1):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создаем три задачи для трех силачей
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    ]

    await asyncio.gather(*tasks)    # Ожидаем завершения всех задач

if __name__ == '__main__':
    asyncio.run(start_tournament())

# Вывод на консоль:
# Силач Pasha начал соревнования
# Силач Denis начал соревнования
# Силач Apollon начал соревнования
# Силач Apollon поднял 1 шар
# Силач Denis поднял 1 шар
# Силач Pasha поднял 1 шар
# Силач Apollon поднял 2 шар
# Силач Denis поднял 2 шар
# Силач Apollon поднял 3 шар
# Силач Pasha поднял 2 шар
# Силач Denis поднял 3 шар
# Силач Apollon поднял 4 шар
# Силач Pasha поднял 3 шар
# Силач Apollon поднял 5 шар
# Силач Apollon закончил соревнования
# Силач Denis поднял 4 шар
# Силач Denis поднял 5 шар
# Силач Denis закончил соревнования
# Силач Pasha поднял 4 шар
# Силач Pasha поднял 5 шар
# Силач Pasha закончил соревнования

