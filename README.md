# wikiwalk
An algorithm that tries to find the shortest 'semantic' path between two topics by navigating links on their respective wikipedia pages.
Currently uses a greedy search algorithm which picks the next link with shortest document distance as measured by cosine similarity in their respective bags of words vector.
