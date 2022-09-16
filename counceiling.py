import os
from supabase import create_client, Client
from flask import Flask, jsonify, request, Response

url = "https://zvxlqpfkfudfdqedqoyu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2eGxxcGZrZnVkZmRxZWRxb3l1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjE5NTY2OTgsImV4cCI6MTk3NzUzMjY5OH0.1MfObcGD01cJhUEJC6sowQ71xWyXD__HNmDcM5ALwig"

supabase = create_client(url, key)

app = Flask(__name__)

def find_approvals(id):
    data = supabase.table("approvals").select("*").eq('id',id ).execute()
    return data['data'] 

def insert_approval(title, project_name, value):
    approval = {
        "title": title,
        "project_name": project_name,
        "value": value
    }

    data = supabase.table("approvals").insert(approval).execute()

    return data['data']

@app.route('/articles/<id>', methods=['POST'])
def add_approval(id):

    data = request.get_json()

    title = data['title']
    project_name = data['project_name']
    value = data['value']

    res = insert_approval(title, project_name, int(value))

    return jsonify(res), 201