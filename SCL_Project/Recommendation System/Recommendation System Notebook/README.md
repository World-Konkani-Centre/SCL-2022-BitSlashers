# Recommendation Engine : WeGroW

System to recommend a given number of products to the user based on <b>similarity and dissimilarity among similar users</b>.


## Framework in Detail

- Input: UserID
- Output: List of ProductIDs to be recommneded

### Algorithm Designed
1. Preprocess data to only required features
2. Find cosine similarity between UserID and other users and append it as a feature to the Dataframe.
3. Sort the data by Cosine Similarity.
4. Extract top N users from the sorted data
5. Make Each Product to an entity [Each product having two parameters: Frequency and Quantity]
6. For user in Users
7. &nbsp;&nbsp;For Product in Products
8. &nbsp;&nbsp;&nbsp;&nbsp;Find cosine similarity between Corresponding Product of Users
9. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store it as a Dataframe with columns ["ReferenceIndex","ProductId","CosineSim"]
10. Sort the Dataframe based on cosinesimilarity
11. Select top M/2 and Bottom M/2 Products from it.
12. Return M product suggestions.

### Concept

We have built this entire Framework on the concept of <b>Collaborative Filtering </b>.

* Collaborative Filtering predict a user's buying habits based on other users’ previous utility with the item.

* Finding similar users using cosine similarity works on the basis of Vectors.
* More the cosine similarity(angle) indicates that there is a larger diviation in the two vectors which in laymans term means they are very different. Whereas a lesser Cosine Similarity indicates similarity between the vectors.<br>
* Once we have the similar users, most similar products allowing multiple occurance of same product as it indicates a users pattern of buying same thing re-assures their user behavior through recommendation.<br>
* Dissimilar Products represent the ones the user has tried out or the peers are using a lot and can be used to create a new buying habit through recommendation.


## Developed by
* [Karthik Pai](https://github.com/kptriescoding)
* [Nanda Kishor M Pai](https://github.com/nandakishormpai)

## References

* [Scipy Cosine Similarity Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html)
* [Recommendation Systems Review](https://towardsdatascience.com/recommendation-systems-a-review-d4592b6caf4b)


