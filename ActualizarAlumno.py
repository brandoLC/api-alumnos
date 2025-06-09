import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    try:
        # Verificar si el alumno existe
        response = table.get_item(
            Key={
                'tenant_id': tenant_id,
                'alumno_id': alumno_id
            }
        )
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({
                    'message': 'Alumno no encontrado'
                })
            }
        
        # Actualizar el alumno
        update_response = table.update_item(
            Key={
                'tenant_id': tenant_id,
                'alumno_id': alumno_id
            },
            UpdateExpression='SET alumno_datos = :datos',
            ExpressionAttributeValues={
                ':datos': alumno_datos
            },
            ReturnValues='UPDATED_NEW'
        )
        
        # Salida (json)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Alumno actualizado exitosamente',
                'tenant_id': tenant_id,
                'alumno_id': alumno_id,
                'updated_attributes': update_response['Attributes']
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
