import boto3
import json
import urllib3

import boto3

def lambda_handler(event, context):
    client = boto3.client('dms')
    response = client.describe_replication_tasks()
    
    tasks_running = []
    for task in response['ReplicationTasks']:
        if task['Status'] == 'running':
            tasks_running.append(task)
    
    # tasks_paused = 0
    # for task in tasks_running:
    #     response = client.stop_replication_task(
    #         ReplicationTaskArn=task['ReplicationTaskArn']
    #     )
    #     tasks_paused += 1
        
    

    
# ------- MatterMost Webhook -------
    http    = urllib3.PoolManager()
    url     = < webhook_url >
    msg = {
        "icon_url" : "https://res.cloudinary.com/hy4kyit2a/f_auto,fl_lossy,q_70/learn/modules/aws-cloud-acquisition/migrate-to-the-aws-cloud/images/7cc5c531c915800ae6dadf9b1945ac30_dbed-345-c-3418-4630-964-c-41-bef-5-a-32-dbd.png",
        "channel": "aws_alerts",
        "username": "AWS Alert",
        "text": "",
        "attachments": [
            { 
                "color": "#047cc4",
                "fields": [
                    {
                        "title": "Conta AWS",
                        "value": "902671150478",
                        "short": True
                    },
                    {
                        "title": "Serviços",
                        "value": "AWS Data Migration Task",
                        "short": True
                    },
                    {
                        "title": "Ambiente",
                        "value": "Stg e Dev",
                        "short": True
                    },
                    {
                        "title": "Status",
                        "value": "Parando tarefas",
                        "short": True
                    }
                ]
            }
        ]
    }
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    
    
    return {
        'message': f"{tasks_paused} tarefas de migração foram pausadas com sucesso."
    }
