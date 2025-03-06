from ast import Tuple


base_config: Tuple = {
    "Co-Host-Speaker-Voice": "af_sky+af_bella",
    "Host-Speaker-Voice": "af_alloy",

    "Small-Text-Model": {
        "provider": {
            "name": "lmstudio",
            "key": "not-needed"
        },
        "model": "llama-3.2-3b-instruct"
    },

    "Big-Text-Model": {
        "provider": {
            "name": "lmstudio",
            "key": "not-needed"
        },
        "model": "llama-3.2-3b-instruct"
    },

    "Text-To-Speech-Model": {
        "provider": {
            "name": "custom",
            "endpoint": "http://localhost:8880/v1",
            "key": "not-needed"
        },
        "model": "kokoro",
        "audio_format": "wav"
    },

    "Step1": {
        "max_tokens": 1028,
        "temperature": 0.7,
        "chunk_size": 1000,
        "max_chars": 100000
    },

    "Step2": {
        "max_tokens": 8126,
        "temperature": 1
    },

    "Step3": {
        "max_tokens": 8126,
        "temperature": 1
    }
}