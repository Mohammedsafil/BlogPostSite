from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This comment inserts data in table"

    def handle(self, *args: Any, **options: Any):
        titles = [
            "The Future of Artificial Intelligence in Everyday Life", "5 Must-Have Productivity Apps for 2024", "Exploring the World's Most Beautiful Destinations", "A Beginner's Guide to Data Science", "Top 10 Tips for a Healthy Lifestyle", "How Blockchain Technology is Revolutionizing Finance", "The Psychology of Happiness: How to Live a Fulfilling Life", "The Rise of Remote Work: Is It Here to Stay?", "10 Simple Recipes for Busy Weeknights", "Mastering Python for Data Analysis", "Sustainability in Fashion: A Growing Trend", "The Importance of Mental Health Awareness", "Tech Gadgets You Need in 2024", "The Ultimate Guide to Starting a Blog in 2024", "How to Stay Fit While Working from Home", "Investing 101: How to Get Started with Stock Market Basics", "The Power of Minimalism: How Less Can Be More", "Cybersecurity in the Digital Age: What You Need to Know", "How to Build Your Personal Brand on LinkedIn", "10 Common Mistakes When Learning to Code (and How to Avoid Them)"
        ]

        contents = [
            "Artificial Intelligence (AI) is rapidly transforming industries, from healthcare to transportation. With advancements in machine learning, AI will soon be embedded in almost every aspect of our daily lives. Explore how AI is shaping the future and what it means for the average person.", "Staying organized can be tough, but these five productivity apps are here to help. Whether you need a task manager or a focus booster, these tools are perfect for streamlining your workflow and making the most of your time.", "Dreaming of your next vacation? From the crystal-clear waters of the Maldives to the breathtaking landscapes of New Zealand, we’ve compiled a list of the most stunning places you should add to your travel bucket list.", "Data science is one of the hottest fields today, but getting started can seem overwhelming. This beginner’s guide covers the essential tools and skills you need to kickstart your journey in data science, including Python, statistics, and machine learning basics.", "Maintaining a healthy lifestyle can be easier than you think. With simple habits like staying hydrated, exercising regularly, and eating balanced meals, you can drastically improve your health and well-being.", "Blockchain is more than just the technology behind cryptocurrencies. It’s changing how we think about transactions, trust, and security in the financial world. Learn how blockchain is disrupting traditional banking and creating new opportunities.", "What does it mean to live a happy and fulfilling life? This post dives into the psychology behind happiness, sharing insights on how to cultivate positive habits, relationships, and mindsets to lead a more meaningful existence.", "With the shift to remote work during the pandemic, many companies are rethinking traditional office models. This article explores the future of remote work and how it is reshaping the global workforce.", "After a long day, the last thing you want is a complicated meal. These 10 quick and easy recipes will have dinner on the table in no time, and they’re perfect for families or anyone with a busy schedule.", "Python is a powerful tool for data analysis, widely used by data scientists. This post covers essential Python libraries such as NumPy, Pandas, and Matplotlib, and walks you through analyzing real-world data sets.", "As consumers become more conscious about environmental impact, sustainability in fashion is gaining momentum. From eco-friendly fabrics to ethical production methods, learn how the fashion industry is evolving to meet these demands.", "Mental health has long been a taboo subject, but today, there’s a growing movement for mental health awareness. This post discusses why it's critical to break the stigma, provide support, and promote well-being for everyone.", "The tech world is constantly evolving, and 2024 is set to bring some incredible innovations. From smart home devices to wearable tech, here’s a roundup of the must-have gadgets that will make life easier.", "Have you ever thought about starting your own blog? Whether it’s a personal passion or a way to share expertise, this guide will walk you through everything from choosing a niche to promoting your content.", "Remote work can take a toll on your physical health if you’re not careful. This post shares practical tips for staying active, avoiding bad posture, and maintaining a fitness routine while working from home.", "The stock market can seem intimidating, but it’s a great way to build wealth over time. This guide covers the basics of investing, from understanding stocks and bonds to how to start your portfolio.", "Minimalism isn’t just a design trend—it’s a lifestyle. By simplifying your life, you can reduce stress, increase focus, and make room for what truly matters. Learn how adopting a minimalist mindset can change your life.", "As our reliance on technology grows, so does the need for robust cybersecurity. This post explains common cybersecurity threats, how to protect yourself online, and what the future holds for data privacy.", "LinkedIn is more than a place to list your resume. It’s a powerful platform for networking and building your personal brand. This article provides tips for optimizing your profile and engaging with the LinkedIn community to stand out professionally.", "Learning to code is challenging, and beginners often make the same mistakes. This post highlights 10 common pitfalls—from focusing on syntax over logic to neglecting practice—and how you can avoid them to become a better programmer."
        ]

        img_uls = [
            " https://picsum.photos/id/1/800/400", "https://picsum.photos/id/2/800/400", "https://picsum.photos/id/3/800/400", "https://picsum.photos/id/4/800/400", "https://picsum.photos/id/5/800/400", "https://picsum.photos/id/6/800/400", "https://picsum.photos/id/7/800/400", "https://picsum.photos/id/8/800/400", "https://picsum.photos/id/9/800/400", "https://picsum.photos/id/10/800/400", "https://picsum.photos/id/11/800/400", "https://picsum.photos/id/12/800/400", "https://picsum.photos/id/13/800/400", "https://picsum.photos/id/14/800/400", "https://picsum.photos/id/15/800/400", "https://picsum.photos/id/16/800/400", "https://picsum.photos/id/17/800/400", "https://picsum.photos/id/18/800/400", "https://picsum.photos/id/19/800/400", "https://picsum.photos/id/20/800/400"
        ]


        for title, content, img_url in zip(titles, contents, img_uls):
            Post.objects.create(title = title, content = content , img_url = img_url)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data..!"))
