# imageProcessing/schema.py
import graphene

class Query(graphene.ObjectType):
    get_data_from_angular = graphene.String(url=graphene.String())

    def resolve_get_data_from_angular(self, info, url):
        # Your logic to fetch data based on the provided URL
        # For simplicity, we'll return a mock JSON response
        response_data = {'message': 'Data fetched successfully', 'url': url}
        return response_data

class Mutation(graphene.ObjectType):
    # Define mutations if needed
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
