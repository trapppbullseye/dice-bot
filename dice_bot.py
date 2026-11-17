#!/usr/bin/env python3
"""Discord dice roller with custom sets"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord dice roller with custom sets")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("dice-bot v0.1.0");return
 print(f"[12:12] dice-bot ready")
if __name__=="__main__":main()
