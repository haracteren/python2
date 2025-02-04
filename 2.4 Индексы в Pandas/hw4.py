import numpy as np
import pandas as pd

# 1. Разобраться, как использовать мультииндексные ключи в данном примере
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2', 'city_3'],
        [2010, 2020]
    ],
    names = ['city', 'year']
)

population = [
    101,
    201,
    102,
    202,
    103,
    203]
pop = pd.Series(population, index=index)

# 2020 год (для всех столбцов)
print(pop.loc[(slice(None), 2020)])


# job_1 (для всех строк)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names = ['worker', 'job']
)
data_df = pd.DataFrame(
    {
        'total': pop,
        'something': [10, 11, 12, 13, 14, 15]
    }, index=index)

print(data_df.xs('job_1', level='job', axis=1))

print(data_df.loc['city_1', (slice(None), 'job_2')])


# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names = ['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)

# 1. Выбор данных за 2020 год (для всех столбцов)
print(data_df.loc[(slice(None), 2020), :])


# 2. Выбор данных по job_1 (для всех строк)
print(data_df.xs('job_1', level='job', axis=1))


# 3. Выбор данных для city_1 и job_2
print(data_df.loc['city_1', (slice(None), 'job_2')])



# 3. Взять за основу DataFrame со следующей структурой . . .

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)
idx = pd.IndexSlice

# 1. Все данные по person_1 и person_3
print(data_df.loc[:, idx[['person_1', 'person_3'], :]])

# 2. Все данные по первому городу и первым двум person-ам
print(data_df.loc['city_1', :].iloc[:, :2])



#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['b', 'c', 'f'], index=[4, 5, 6])

print(pd.concat([ser1, ser2], join='outer'))

print(pd.concat([ser1, ser2], join='inner'))
