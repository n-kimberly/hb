from unittest import TestCase, mock
import restaurantcli as rcli
import restaurantratings as rr


class CLITestCase(TestCase):
    """Tests for our Restaurant CLI"""

    def setUp(self):
        self.ratings = rr.RestaurantRatings([
            rr.RestaurantRating("The Tavern", 10),
            rr.RestaurantRating("Gastropub", 7)
        ])

    def test_get_ratings(self):
        # Create mock method that returns ratings attr

        def mock_get_ratings_from_file(filename):
            return self.ratings

        with mock.patch(
                "restaurantratings.RestaurantRatings.get_ratings_from_file",
                mock_get_ratings_from_file) as m:

            ratings = rr.RestaurantRatings.get_ratings_from_file("mockfile")

        self.assertEqual(len(ratings.ratings), 2)
        self.assertEqual(ratings.ratings[0].name, "The Tavern")
        self.assertEqual(ratings.ratings[0].rating, 10)
        self.assertEqual(ratings.ratings[1].name, "Gastropub")
        self.assertEqual(ratings.ratings[1].rating, 7)


class RestaurantRatingTests(TestCase):
    """Tests for individual restaurant rating objects"""

    def test_init(self):
        rating = rr.RestaurantRating("The Tavern", 10)
        self.assertEqual(rating.name, "The Tavern")
        self.assertEqual(rating.rating, 10)

    def test_update_rating(self):
        rating = rr.RestaurantRating("The Tavern", 10)
        rating.update_rating(2)
        self.assertEqual(rating.rating, 2)

    def test_eq_true(self):
        rating_1 = rr.RestaurantRating("The Tavern", 10)
        rating_2 = rr.RestaurantRating("Gastropub", 10)
        self.assertEqual(rating_1, rating_2)

    def test_eq_false(self):
        rating_1 = rr.RestaurantRating("The Tavern", 10)
        rating_2 = rr.RestaurantRating("Gastropub", 9)
        self.assertNotEqual(rating_1, rating_2)

    def test_lt_true(self):
        rating_1 = rr.RestaurantRating("The Tavern", 9)
        rating_2 = rr.RestaurantRating("Gastropub", 10)
        self.assertLess(rating_1, rating_2)

    def test_lt_false(self):
        rating_1 = rr.RestaurantRating("The Tavern", 10)
        rating_2 = rr.RestaurantRating("Gastropub", 9)
        self.assertFalse(rating_1 < rating_2)


class RestaurantRatingsTests(TestCase):
    """Tests for the RestaurantRatingsTests umbrella objects"""

    def setUp(self):
        """Set up sub-objects for RestaurantRatings tests"""
        self.ratings = rr.RestaurantRatings([
            rr.RestaurantRating("The Tavern", 10),
            rr.RestaurantRating("Gastropub", 9),
            rr.RestaurantRating("Snack Shack", 5)
        ])

    def test_init(self):
        rrobj = rr.RestaurantRatings()
        self.assertEqual(len(rrobj.ratings), 0)
        self.assertEqual(rrobj.ratings, [])

    def test_init_with_source(self):
        rrobj = rr.RestaurantRatings([rr.RestaurantRating("The Tavern", 10)])
        self.assertEqual(len(rrobj.ratings), 1)
        self.assertEqual(rrobj.ratings[0].name, "The Tavern")
        self.assertEqual(rrobj.ratings[0].rating, 10)

if __name__ == "__main__":

    import unittest

    unittest.main()
