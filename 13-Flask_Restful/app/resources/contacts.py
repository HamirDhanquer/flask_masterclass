from flask_restful import Resource, marshal
from app.models import Contact
from app import request, db
from app.schemas import contact_field

class Contacts(Resource):

    def get(self):
        contacts = Contact.query.all()
        return marshal(contacts,contact_field,"contacts")


    def post(self):
        payload = request.only(["name","cellphone"]) 
        name = payload["name"]
        cellphone = payload["cellphone"]

        contacts = Contact(name,cellphone)
        db.session.add(contacts)
        db.session.commit()
        return marshal(contacts,contact_field,"contacts")


    def put(self):
        payload = request.only(["id","name","cellphone"])
        _id = payload["id"]
        name=payload["name"]
        cellphone = payload["cellphone"]

        contact = Contact.query.get(_id)
        
        if not contact:
            return {"message":"O Id requisitado não existe"}

        contact.name = name
        contact.phone = cellphone

        db.session.add(contact)
        db.session.commit()
        return marshal(contact, contact_field, "contact")

    def delete(self):
        payload = request.only(["id"])
        _id = payload["id"]

        contact = Contact.query.get(_id)

        if not contact:
            return {"message":"O Id requisitado não existe"}

        db.session.delete(contact)
        db.session.commit()
        return marshal(contact,contact_field,"contact")