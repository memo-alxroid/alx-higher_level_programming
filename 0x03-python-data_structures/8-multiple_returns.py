#!/usr/bin/python3

def multiple_returns(sentence):
    return len(sentence) if sentence else 0,sentence[0] if sentence else None
