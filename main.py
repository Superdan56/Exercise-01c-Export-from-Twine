#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "passages": [
    {
      "text": "This is an open field west of a white house, with a boarded front door.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[WEST->Forest]]",
      "links": [
        {
          "name": "NORTH",
          "link": "North of House",
          "pid": "2"
        },
        {
          "name": "SOUTH",
          "link": "South of House",
          "pid": "3"
        },
        {
          "name": "WEST",
          "link": "Forest",
          "pid": "4"
        }
      ],
      "name": "West of House",
      "pid": "1",
      "position": {
        "x": "412",
        "y": "189"
      }
    },
    {
      "text": "You are facing the north side of a white house. There is no door here, and all the windows are barred.\n\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[NORTH->Forest]]\n",
      "links": [
        {
          "name": "WEST",
          "link": "West of House",
          "pid": "1"
        },
        {
          "name": "EAST",
          "link": "East of House",
          "pid": "5"
        },
        {
          "name": "NORTH",
          "link": "Forest",
          "pid": "4"
        }
      ],
      "name": "North of House",
      "pid": "2",
      "position": {
        "x": "262",
        "y": "339"
      }
    },
    {
      "text": "You are facing the south side of a white house. There is no door here, and all the windows are barred.\n\n[[WEST->West of House]]\n[[EAST->East of House]]\n[[SOUTH->Forest]]",
      "links": [
        {
          "name": "WEST",
          "link": "West of House",
          "pid": "1"
        },
        {
          "name": "EAST",
          "link": "East of House",
          "pid": "5"
        },
        {
          "name": "SOUTH",
          "link": "Forest",
          "pid": "4"
        }
      ],
      "name": "South of House",
      "pid": "3",
      "position": {
        "x": "412",
        "y": "339"
      }
    },
    {
      "text": "This is a forest, with trees in all directions around you.\n\n[[NORTH->Sunlit Forest]]\n[[EAST->Forest]]\n[[SOUTH->Forest]]\n[[WEST->Forest]]",
      "links": [
        {
          "name": "NORTH",
          "link": "Sunlit Forest",
          "pid": "6"
        },
        {
          "name": "EAST",
          "link": "Forest",
          "pid": "4"
        },
        {
          "name": "SOUTH",
          "link": "Forest",
          "pid": "4"
        },
        {
          "name": "WEST",
          "link": "Forest",
          "pid": "4"
        }
      ],
      "name": "Forest",
      "pid": "4",
      "position": {
        "x": "562",
        "y": "339"
      }
    },
    {
      "text": "You are behind the white house. A path leads into the forest to the east. In one corner of the house there is a small window which is slightly ajar.\n\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[EAST->Sunlit Forest]]\n[[WEST->Kitchen]]\n[[ENTER->Kitchen]]",
      "links": [
        {
          "name": "NORTH",
          "link": "North of House",
          "pid": "2"
        },
        {
          "name": "SOUTH",
          "link": "South of House",
          "pid": "3"
        },
        {
          "name": "EAST",
          "link": "Sunlit Forest",
          "pid": "6"
        },
        {
          "name": "WEST",
          "link": "Kitchen",
          "pid": "7"
        },
        {
          "name": "ENTER",
          "link": "Kitchen",
          "pid": "7"
        }
      ],
      "name": "East of House",
      "pid": "5",
      "position": {
        "x": "262",
        "y": "489"
      }
    },
    {
      "text": "This is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\n\n[[NORTH->Forest]]\n[[SOUTH->Forest]]\n[[EAST->Forest]]\n[[WEST->East of House]]\n[[UP->Tree]]",
      "links": [
        {
          "name": "NORTH",
          "link": "Forest",
          "pid": "4"
        },
        {
          "name": "SOUTH",
          "link": "Forest",
          "pid": "4"
        },
        {
          "name": "EAST",
          "link": "Forest",
          "pid": "4"
        },
        {
          "name": "WEST",
          "link": "East of House",
          "pid": "5"
        },
        {
          "name": "UP",
          "link": "Tree",
          "pid": "8"
        }
      ],
      "name": "Sunlit Forest",
      "pid": "6",
      "position": {
        "x": "562",
        "y": "489"
      }
    },
    {
      "text": "You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\n\n[[EAST->East of House]]",
      "links": [
        {
          "name": "EAST",
          "link": "East of House",
          "pid": "5"
        }
      ],
      "name": "Kitchen",
      "pid": "7",
      "position": {
        "x": "262",
        "y": "639"
      }
    },
    {
      "text": "You are about 10 feet above the ground nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\n\n[[DOWN->Sunlit Forest]]",
      "links": [
        {
          "name": "DOWN",
          "link": "Sunlit Forest",
          "pid": "6"
        }
      ],
      "name": "Tree",
      "pid": "8",
      "position": {
        "x": "562",
        "y": "639"
      }
    }
  ],
  "name": "Zork",
  "startnode": "1",
  "creator": "Twine",
  "creator-version": "2.3.14",
  "ifid": "216ACD94-C70D-42CE-80F1-FA90A0D7F747"
}

if "name" in world and "passages" in world:
    print(world["name"])
    print()
    for passage in world["passages"]:
        print(passage["name"])
        print(passage["cleanText"])
        for link in passage["links"]:
            print(link["linkText"])
        print()