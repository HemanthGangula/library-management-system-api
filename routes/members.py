from flask import Blueprint, request, jsonify
from typing import List, Optional
from models import Member

bp = Blueprint('members', __name__, url_prefix='/members')

# In-memory storage for members
members: List[Member] = []

@bp.route('/', methods=['GET'])
def get_members():
    return jsonify([member.__dict__ for member in members]), 200

@bp.route('/', methods=['POST'])
def add_member():
    data = request.get_json()
    member = Member(
        id=len(members) + 1,
        name=data.get('name'),
        email=data.get('email')
    )
    members.append(member)
    return jsonify(member.__dict__), 201

@bp.route('/<int:member_id>', methods=['GET'])
def get_member(member_id: int):
    member: Optional[Member] = next((m for m in members if m.id == member_id), None)
    if member:
        return jsonify(member.__dict__), 200
    return jsonify({'message': 'Member not found'}), 404

@bp.route('/<int:member_id>', methods=['PUT'])
def update_member(member_id: int):
    data = request.get_json()
    member: Optional[Member] = next((m for m in members if m.id == member_id), None)
    if member:
        member.name = data.get('name', member.name)
        member.email = data.get('email', member.email)
        return jsonify(member.__dict__), 200
    return jsonify({'message': 'Member not found'}), 404

@bp.route('/<int:member_id>', methods=['DELETE'])
def delete_member(member_id: int):
    global members
    members = [m for m in members if m.id != member_id]
    return jsonify({'message': 'Member deleted'}), 200