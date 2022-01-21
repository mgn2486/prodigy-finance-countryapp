from email import message
from typing_extensions import Required
from urllib import response
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

country_put_args = reqparse.RequestParser()
country_put_args.add_argument("name", type=str, help="Name of the country is required", required = True )
country_put_args.add_argument("alpha2code", type=str, help="alpha 2 code of the country is required", required = True )
country_put_args.add_argument("alpha3code", type=str, help="alpha 3 code on the country is required", required = True )
country_put_args.add_argument("currency", type=str, help="currency of the country is required", required = True )


countries = {  }

def abort_if_country_doesnt_exist(country_id):
    if country_id not in countries:
        abort(404, message = "Sorry country could not be found...")

def abort_if_country_exists(country_id):
    if(country_id in countries):
        abort(409, message="Sorry this country already exists")



class CountryController(Resource):
    def get(self, country_id):
        abort_if_country_doesnt_exist(country_id)
        return countries[country_id]

    def put(self, country_id):
        abort_if_country_exists(country_id)
        args = country_put_args.parse_args()
        countries[country_id] = args
        return countries[country_id], 201

    def delete(self, country_id):
        abort_if_country_doesnt_exist(country_id)
        del countries[country_id]
        return '',204

api.add_resource(CountryController, "/country/<int:country_id>")

class CountryControllerByCountryName(Resource):

    def get(self, country_name):
        for x in countries:
            if countries[x].name == country_name:
                response = countries[x]
        return response

api.add_resource(CountryControllerByCountryName, "/country/name/<string:country_name>")

class CountryControllerByAphaCode2(Resource):
    
    def get(self, country_alpha2code):
        for x in countries:
            if countries[x].alpha2code == country_alpha2code:
                response = countries[x]
        return response

api.add_resource(CountryControllerByAphaCode2, "/country/alphacode/2/<string:country_alpha2code>")


class CountryControllerByAphaCode3(Resource):
    
    def get(self, country_alpha3code):
        for x in countries:
            if countries[x].alpha3code == country_alpha3code:
                response = countries[x]
        
        return response

api.add_resource(CountryControllerByAphaCode3, "/country/alphacode/3/<string:country_alpha3code>")

class CountryControllerByCurrency(Resource):
    
    def get(self, country_currency):
        for x in countries:
            if countries[x].currency == country_currency:
                response = countries[x]        
                return response

api.add_resource(CountryControllerByCurrency, "/country/currency/<string:country_currency>")


if __name__ == "__main__":
    app.run(debug =True)
