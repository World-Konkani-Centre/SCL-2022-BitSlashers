# Recommendation Engine

System to recommend a given number of products to the user based on <b>similarity and dissimilarity among similar users</b>.

## Developed by
* [Karthik Pai](https://github.com/kptriescoding)
* [Nanda Kishor M Pai](https://github.com/nandakishormpai)

## Framework in Detail

- Input: UserID
- Output: List of ProductIDs to be recommneded

### Algorithm Designed
1. Preprocess data to only required features
2. Find cosine similarity between UserID and other users and add it as a feature.
3. Sort the data by Cosine Similarity.
4. Extract top N users from the sorted data
5. Make Each Product to an entity
6. For user in Users
7.     For Product in Products
8.          Find cosine similarity between Corresponding Product of Users
9.          Store it as a 




