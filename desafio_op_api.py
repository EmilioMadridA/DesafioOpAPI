# Librerias
import requests

# URL base de la API
url = "https://reqres.in/api/users"

# Se inicializa la variable para poder acceder a la data de la API
users_data = {'data': []}

# 1. Obtener toda la información de los usuarios de todas las páginas
# Ciclo for para recorrer las páginas de la API
for i in range(1,3):
    response = requests.get(url, params = {'page': i})
    if response.status_code == 200:
        data = response.json()
        users_data['data'].extend(data['data'])
    else:
        print(f'{response.status_code}')
# Impresion de la variable con los datos ingresados
print(users_data['data'])

# 2. Crear un usuario
nuevo_usuario = {'first_name': 'Ignacio', 'job': 'Profesor'}
response = requests.post(url, data=nuevo_usuario)
if response.status_code in range(200, 300):
    created_user = response.json()
else:
    print(f'{response.status_code}')
# Impresion del usuario creado, con sus claves y valores correspondientes
print(created_user)

# 3. Actualizar/Crear usuario
nuevo_usuario2 = {'first_name': 'morpheus', 'residence': 'zion'}
response = requests.post(url, data=nuevo_usuario2)
if response.status_code in range(200, 300):
    updated_user = response.json()
else:
    print(f'{response.status_code}')
# Impresion del usuario creado/actualizado, con sus claves y valores correspondientes
print(updated_user)

# 4. Eliminar usuario
# Filtrado de los datos para eliminar el usuario indicado
data_filtrada = [user for user in users_data['data'] if user.get('first_name') != 'Tracey']
print(data_filtrada)