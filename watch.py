import re
import sys

# the user input example: <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
def main():
    s = input("HTML: ").strip()
    print(parse(s))


def parse(s):
    pattern = r'"(?:https?)?://(?:www\.)?youtube\.com/embed/([^"]*)"'
    matches = re.search(pattern, s)
    if matches:
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"

if __name__ == "__main__":
    main()
