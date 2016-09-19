#!/usr/bin/env python

import rdflib

g = rdflib.Graph()
g.parse("menus.json", format="json-ld")

g.serialize(open("menus.rdf", "w"), format="xml")
g.serialize(open("menus.ttl", "w"), format="turtle")

