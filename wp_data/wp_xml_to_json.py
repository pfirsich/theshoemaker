from lxml import etree
import argparse
import json
import os

# thank you: https://github.com/bendemaree/python-wordpressparse/blob/master/parse.py


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputxml")
    args = parser.parse_args()

    tree = etree.parse(args.inputxml)

    root = tree.getroot()
    ns = root.nsmap

    get_child = lambda parent, name: parent.find("./" + name, namespaces=ns).text

    jout = {}

    print("# Posts")
    jout["posts"] = []
    posts = tree.findall(".//item[wp:post_type='post']", namespaces=ns)
    for post in posts:
        jpost = {}
        jpost["id"] = get_child(post, "./wp:post_id")
        jpost["title"] = get_child(post, "./title")
        print(jpost["id"], jpost["title"])
        jpost["link"] = get_child(post, "./link")
        jpost["pub_date"] = get_child(post, "./pubDate")
        assert get_child(post, "./dc:creator") == "joel"
        assert get_child(post, "./description") == None
        jpost["content"] = get_child(post, "./content:encoded")
        assert len(get_child(post, "./excerpt:encoded")) == 0
        # I need both because sometimes one of them is 0000-00-00 00:00:00
        jpost["post_date"] = get_child(post, "./wp:post_date")
        jpost["post_date_gmt"] = get_child(post, "./wp:post_date_gmt")
        jpost["name"] = get_child(post, "./wp:post_name")
        jpost["status"] = get_child(post, "./wp:status")

        jpost["tags"] = []
        for tag in post.findall("./category[@domain='post_tag']"):
            jpost["tags"].append(tag.get("nicename"))

        # postmeta seems to be uninteresting

        jpost["comments"] = []
        for comment in post.findall("./wp:comment", namespaces=ns):
            jcomment = {}
            jcomment["id"] = get_child(comment, "wp:comment_id")
            jcomment["author"] = get_child(comment, "wp:comment_author")
            jcomment["author_email"] = get_child(comment, "wp:comment_author_email")
            jcomment["date_gmt"] = get_child(comment, "wp:comment_date_gmt")
            jcomment["content"] = get_child(comment, "wp:comment_content")
            jcomment["parent"] = get_child(comment, "wp:comment_parent")
            jpost["comments"].append(jcomment)

        jout["posts"].append(jpost)

    print()
    print("# Attachments")
    jout["attachments"] = []
    attachments = tree.findall(".//item[wp:post_type='attachment']", namespaces=ns)
    for attachment in attachments:
        jattachment = {}
        jattachment["id"] = get_child(attachment, "wp:post_id")
        jattachment["title"] = get_child(attachment, "title")
        print(jattachment["id"], jattachment["title"])
        jattachment["content"] = get_child(attachment, "content:encoded")
        jattachment["excerpt"] = get_child(attachment, "excerpt:encoded")
        jattachment["url"] = get_child(attachment, "wp:attachment_url")
        jout["attachments"].append(jattachment)

    out_file = os.path.splitext(args.inputxml)[0] + ".json"
    with open(out_file, "w") as f:
        json.dump(jout, f, indent=4)


if __name__ == "__main__":
    main()
