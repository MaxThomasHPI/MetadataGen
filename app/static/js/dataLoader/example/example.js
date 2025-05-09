const example1 = {
    "name": "Test",
    "learningResourceType": {
        "identifier": "https://w3id.org/kim/hcrt/course",
        "type": "Concept",
        "inScheme": "https://w3id.org/kim/hcrt/scheme"
    },
    "description": "This is the course",
    "publisher": {
        "name": "pub",
        "url": "https://www.example.com",
        "description": "A test description for the publisher.",
        "type": "Organization"
    },
    "creator": [
        {
            "name": "John Doe",
            "honorificPrefix": "Prof. Dr.",
            "description": "This is Prof. Dr. John Doe",
            "type": "Person"
        },
        {
            "name": "Joan Doe",
            "description": "This is Joan Doe",
            "type": "Person"
        },
        {
            "name": "Sam T. Est",
            "type": "Person"
        }
    ],
    "url": "https://www.my-course.org",
    "license": [
        {
            "identifier": "CC-BY-4.0",
            "url": "https://spdx.org/licenses/CC-BY-4.0.html"
        }
    ],
    "startDate": [
        "2025-03-20T12:00:00"
    ],
    "endDate": [
        "2025-04-19T12:00:00"
    ],
    "educationalAlignment": [
        {
            "name": [
                {
                    "name": "software and applications development and analysis",
                    "inLanguage": "en"
                }
            ],
            "educationalFramework": "ISCED-F",
            "type": "educationalSubject",
            "educationalFrameworkVersion": "2013"
        }
    ],
    "teaches": [
        {
            "name": [
                {
                    "name": "COLLABORATING THROUGH DIGITAL TECHNOLOGIES",
                    "inLanguage": "en"
                }
            ],
            "educationalFramework": "DigComp",
            "educationalFrameworkVersion": "2.2"
        },
        {
            "name": [
                {
                    "name": "BROWSING, SEARCHING AND FILTERING DATA, INFORMATION AND DIGITAL CONTENT",
                    "inLanguage": "en"
                }
            ],
            "educationalFramework": "DigComp",
            "educationalFrameworkVersion": "2.2"
        },
        {
            "name": [
                {
                    "name": "providing health care or medical treatments",
                    "inLanguage": "en"
                }
            ],
            "educationalFramework": "ESCO",
            "conceptUrl": "http://data.europa.eu/esco/skill/0a400212-8693-4b1f-b0ca-d1f82c321916",
            "educationalFrameworkVersion": "2.2",
            "url": "https://esco.ec.europa.eu/en/classification/skill_main#overlayspin"
        }
    ],
    "keywords": [
        "keyword1",
        "keyword2",
        "another keyword"
    ],
    "educationalLevel": [{
        "name": [
            {
                "name": 3,
                "inLanguage": "en"
            }
        ],
        "educationalFramework": "DigComp",
        "educationalFrameworkVersion": "2.2",
        "type": "EducationalLevel"
    }]
}

const example2 = {
    "name": "Sustainability in the Digital Age: Efficient AI Techniques in the LLM Era",
    "learningResourceType": {
        "identifier": "https://w3id.org/kim/hcrt/course",
        "type": "Concept",
        "inScheme": "https://w3id.org/kim/hcrt/scheme"
    },
    "description": "<h2>Welcome to the \"Sustainability in the Digital Age\" series</h2>\\n\\n<p>In an era where " +
        "digital technologies are reshaping industries and daily life, the environmental impact of AI systems has " +
        "become a growing concern. This course explores efficient AI methodologies to address these challenges. From " +
        "deep learning model compression to low-bit quantization and collaborative inference, we delve into techniques " +
        "that enhance computational efficiency and reduce energy consumption. In Week 2, we focus on low-bit " +
        "quantization specifically for large language models (LLMs), showcasing cutting-edge open-source tools and " +
        "models. Join us to learn how to build sustainable AI systems while pushing the boundaries of innovation." +
        "</p>\\n\\n<hr>\\n\\n<p>This course is part of the <strong>Sustainability in the Digital Age</strong> series, " +
        "a collaborative project between colleagues from Stanford University, SAP and the Hasso Plattner Institute. </p>\\n",
    "publisher": {
        "name": "openHPI",
        "url": "https://open.hpi.de",
        "description": "openHPI is the digital education platform of the Hasso Plattner Institute, Potsdam, Germany. " +
            "On openHPI you take part in a worldwide social learning network based on interactive online courses " +
            "covering different subjects in Information and Communication Technology (ICT).",
        "type": "Organization"
    },
    "creator": [
        {
            "name": "Haojin Yang",
            "honorificPrefix": null,
            "description": "PD Dr. Haojin Yang is a senior researcher and multimedia and machine learning (MML) " +
                "research group leader at Hasso-Plattner-Institute (HPI). Since 2019, he has been habilitated for a " +
                "professorship. His research focuses on efficient deep learning, model acceleration and compression, " +
                "and AI agentic systems.",
            "type": "Person"
        },
    ],
    "url": "https://open.hpi.de/courses/aimethods2025",
    "license": [
        {
            "identifier": "CC-BY-NC-SA-4.0",
            "url": "https://spdx.org/licenses/CC-BY-NC-SA-4.0.html"
        }
    ],
    "startDate": [
        "2025-05-27T08:00:00Z"
    ],
    "endDate": [
        "2025-06-10T23:55:00Z"
    ]
}


export function getExample(number) {
    switch (number) {
        case 1:
            return example1;
        case 2:
            return example2;
        default:
            return null;
    }
}