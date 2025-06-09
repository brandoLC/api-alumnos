import boto3
import json

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    try:
        tenant_id = event['body']['tenant_id']
        alumno_id = event['body']['alumno_id']
        alumno_datos = event['body']['alumno_datos']
        
        # Proceso
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('t_alumnos')
        
        # Verificar si el alumno ya existe
        existing_item = table.get_item(
            Key={
                'tenant_id': tenant_id,
                'alumno_id': alumno_id
            }
        )
        
        if 'Item' in existing_item:
            return {
                'statusCode': 409,
                'body': json.dumps({
                    'message': 'El alumno ya existe'
                })
            }
        
        alumno = {
            'tenant_id': tenant_id,
            'alumno_id': alumno_id,
            'alumno_datos': alumno_datos
        }
        response = table.put_item(Item=alumno)
        
        # Salida (json)
        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Alumno creado exitosamente',
                'tenant_id': tenant_id,
                'alumno_id': alumno_id,
                'alumno_datos': alumno_datos
            })
        }
        
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': f'Falta el parámetro requerido: {str(e)}'
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error interno del servidor',
                'error': str(e)
            })
        }
