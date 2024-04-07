# from diffusers import StableDiffusionPipeline
from transformers import pipeline
# import torch


def run_chatbot(user_question):

    json_context = {
        "title": "Why did the Bitcoin price drop?",
        "url": "https://readwrite.com/why-did-bitcoin-drop/",
        "publishedAt": "2024-03-15T12:38:50Z",
        "content" : """
    Apple Inc. is a multinational technology company headquartered in Cupertino, California. Founded by Steve Jobs, Steve Wozniak, and Ronald Wayne on April 1, 1976, Apple has become one of the most iconic and influential companies in the world.

    Apple is renowned for its innovative products, including the iPhone, iPad, Mac computers, Apple Watch, and various software and services. The company's commitment to design excellence, user experience, and ecosystem integration has helped it establish a loyal customer base and dominate several markets.

    The iPhone, introduced in 2007, revolutionized the smartphone industry and propelled Apple to unprecedented success. With each new iteration, the iPhone continues to set standards for performance, camera quality, and software capabilities, driving significant advancements in mobile technology.

    In addition to hardware, Apple is a major player in the software and services space. The iOS and macOS operating systems power millions of devices worldwide, providing seamless integration across Apple's product lineup. Services like iCloud, Apple Music, and the App Store contribute significantly to the company's revenue and ecosystem growth.

    Apple's retail stores, known for their sleek design and exceptional customer service, play a crucial role in the company's success. With over 500 locations across 25 countries, Apple Stores serve as hubs for product demonstrations, technical support, and community engagement, further enhancing the brand's visibility and customer experience.

    Beyond its consumer products, Apple is committed to sustainability and environmental responsibility. The company aims to achieve carbon neutrality across its supply chain and product lifecycle by 2030, investing in renewable energy, recycling initiatives, and eco-friendly manufacturing practices.

    Despite its immense success, Apple has faced its share of challenges and controversies. Issues related to labor practices in its supply chain, antitrust concerns regarding the App Store, and privacy debates surrounding user data collection have sparked criticism and regulatory scrutiny.

    Nevertheless, Apple's financial performance remains robust, with consistently high revenues and profits. The company's market capitalization frequently ranks among the highest in the world, reflecting investor confidence in its long-term growth prospects and ability to innovate.

    Looking ahead, Apple continues to push the boundaries of technology with ambitious projects in augmented reality, artificial intelligence, and autonomous vehicles. The upcoming releases of new hardware and software products, as well as advancements in services like Apple TV+ and Apple Arcade, indicate a bright future for the company and its customers.

    In summary, Apple Inc. stands as a symbol of innovation, creativity, and excellence in the technology industry. From its humble beginnings in a garage to its status as a trillion-dollar corporation, Apple's journey embodies the power of visionary leadership, cutting-edge technology, and unwavering dedication to customer satisfaction.
    """
    }

    json_content = json_context['content']
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-large-squad2")

    answer=qa_pipeline({
        'question':user_question,
        'context':json_content
    })

    return answer['answer']