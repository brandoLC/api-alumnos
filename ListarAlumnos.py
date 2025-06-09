import boto3  # import Boto3
import json
from boto3.dynamodb.conditions import Key  # import Boto3 conditions

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    try:
        tenant_id = event['body']['tenant_id']
        
        # Proceso
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('t_alumnos')
        response = table.query(
            KeyConditionExpression=Key('tenant_id').eq(tenant_id)
        )
        items = response['Items']
        num_reg = response['Count']
        print(items)
        
        # Salida (json)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'tenant_id': tenant_id,
                'num_reg': num_reg,
                'alumnos': items
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
