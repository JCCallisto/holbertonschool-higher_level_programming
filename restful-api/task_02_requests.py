import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()

            for post in posts:
                print(post['title'])
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching posts: {e}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()

            structured_posts = [
                {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                }
                for post in posts
            ]

            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(structured_posts)

            print(f"Successfully saved {len(structured_posts)} posts to posts.csv")

        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching posts: {e}")
    except IOError as e:
        print(f"Error occurred while writing to CSV file: {e}")
