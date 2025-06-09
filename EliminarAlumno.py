import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    try:
        # Verificar si el alumno existe antes de eliminarlo
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
        
        # Eliminar el alumno
        delete_response = table.delete_item(
            Key={
                'tenant_id': tenant_id,
                'alumno_id': alumno_id
            },
            ReturnValues='ALL_OLD'
        )
        
        # Salida (json)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Alumno eliminado exitosamente',
                'tenant_id': tenant_id,
                'alumno_id': alumno_id,
                'deleted_item': delete_response.get('Attributes', {})
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
