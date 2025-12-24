{
    "value": 2.217437,
    "description": "sum of:",
    "details": [
    {
        "value": 2.217437,
        "description": "weight(content_ltks:秀才 in 2) [PerFieldSimilarity], result of:",
        "details": [
        {
            "value": 2.217437,
            "description": "score(freq=4.0), computed as boost * idf * tf from:",
            "details": [
            {
                "value": 2.2,
                "description": "boost",
                "details": []
            },
            {
                "value": 1.2953225,
                "description": "idf, computed as log(1 + (N - n + 0.5) / (n + 0.5)) from:",
                "details": [
                {
                    "value": 11,
                    "description": "n, number of documents containing term",
                    "details": []
                },
                {
                    "value": 41,
                    "description": "N, total number of documents with field",
                    "details": []
                }
                ]
            },
            {
                "value": 0.7781274,
                "description": "tf, computed as freq / (freq + k1 * (1 - b + b * dl / avgdl)) from:",
                "details": [
                {
                    "value": 4.0,
                    "description": "freq, occurrences of term within document",
                    "details": []
                },
                {
                    "value": 1.2,
                    "description": "k1, term saturation parameter",
                    "details": []
                },
                {
                    "value": 0.75,
                    "description": "b, length normalization parameter",
                    "details": []
                },
                {
                    "value": 200.0,
                    "description": "dl, length of field (approximate)",
                    "details": []
                },
                {
                    "value": 214.14635,
                    "description": "avgdl, average length of field",
                    "details": []
                }
                ]
            }
            ]
        }
        ]
    }
    ]
}