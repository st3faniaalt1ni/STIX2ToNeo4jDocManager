# Overview

 
# STiX2.0 To Neo4j Doc Manager

The aim of this project is to use a polyglot persistence which, in this case, stores JSON documents in MongoDB, while querying the relationships between the data, using Neo4j graph database. This procedure can be achieved by using the Neo4j Doc Manager for Mongo Connector. In fact, it is a tool that empowers MongoDB developers to migrate documents from MongoDB to a Neo4j property graph structure. Specifically, while Neo4j Doc Manager is running in background, the STIX 2.0 documents that are stored in MongoDB, are imported to a graph concurrently.

Neo4j Doc Manager is based upon Mongo Connector, which requires creating a MongoDB replica set. An OplogThread thread then will listen to all CRUD operations (Create,Read,Update,Delete) occurring in MongoDB. The mongo-connector provides an interface to collect the events caught by the OplogThread. The communication interface is implemented into a structure called DocManager, which can properly receive and handle Mongo documents and information about the database and its collections.




# Installation Instructions and Usage


~~~
git clone
~~~

First, install the project dependencies:
~~~
pip install -r requirements.txt
~~~


















MongoDB configuration:
A mongodb running instance is required. 

Ensure that mongo is running a *replica set*. To initiate a replica set start mongo with:
~~~	 	 	 	
mongod  --port 27018 --replSet myDevReplSet
~~~
Then open mongo shell on port 27018 and run:
~~~
rs.initiate()
~~~

For Neo4j docker Image:

Make sure that you have Docker and Docker-Compose installed.
Then run with sudo privileges:

~~~
docker run --name <container_name> -p7474:7474 -p7687:7687 -d -v /path/to/host/selected/directory/data:/data -v /path/to/host/selected/directory/logs:/logs -v /path/to/host/selected/directory/import:/var/lib/neo4j/import -v /path/to/host/selected/directory j/plugins:/plugins --env NEO4J_AUTH=<neo4j_instance_username>/< neo4j_instance_password> neo4j:latest
~~~


# For Neo4j-Doc-Manager:

You must have Python installed. Python 3 is recommended.
~~~
sudo apt install python3-pip
~~~

Then, install neo4j_doc_manager with pip3:
~~~
pip3 install neo4j-doc-manager
~~~
(You might need sudo privileges).


 Set  **NEO4J_AUTH** environment variable, containing  user and password. Username and password must be the same as the environment variables of neo4j container as they have been initiated on previous step.
~~~
export NEO4J_AUTH=<neo4j_instance_username>/< neo4j_instance_password>

~~~

Start the mongo-connector service with the following command:
~~~
mongo-connector -m localhost:27018 -t http://localhost:7474/db/data -d neo4j_doc_manager
~~~
**-m** provides Mongo endpoint
**-t** provides Neo4j endpoint. Be sure to specify the protocol (http).
**-d** specifies Neo4j Doc Manager.



# Data synchronization

With the REST API and the “neo4j_doc_manager” service running, Stix 2.0 JSON-based documents inserted into MongoDB will be converted into a graph structure and immediately inserted into Neo4j as well. Neo4j Doc Manager will turn keys into graph nodes. Nested values on each key will become properties.










Resources

* [STIX 2.0 Examples](https://oasis-open.github.io/cti-documentation/stix/examples.html)
* [Full Documentation](http://neo4j.com/developer/neo4j-doc-manager/)
* [Neo4j Doc Manager Getting Started](http://neo4j.com/developer/mongodb/)
* [Neo4j Doc Manager: Polyglot Persistence for MongoDB and Neo4j](http://neo4j.com/blog/neo4j-doc-manager-polyglot-persistence-mongodb/) (blog post)

