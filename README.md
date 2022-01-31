# wikiwalk
An algorithm that tries to find the shortest 'semantic' path between two topics by navigating links on their respective wikipedia pages.
Currently uses a greedy search algorithm that picks the next link with shortest document distance as computed using the angle between 
the 'word count' vectors of two articles.
