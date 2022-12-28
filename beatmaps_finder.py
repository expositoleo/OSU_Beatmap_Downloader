from abc import ABC, abstractmethod


class BeatmapsFinderFactory:
    def create_beatmap_finder(self, inputs):
        "Beatmap Finder Strategy Logic goes here"
        if inputs == "ByFilter":
            print("ByFilter")
            return ByFilter()
        elif inputs == "ByUser":
            print("ByUser")
            return ByUser()
        else:
            raise ValueError("Invalid input")


class BeatmapsFinder(ABC):
    @abstractmethod
    def find_beatmaps(self, data):
        pass


"""
CLASS TEMPLATE:

class ?BeatmapsFinder:
    def find_beatmaps(self, data):
        "Logic goes here"
        return beatmaps_list

"""


class UserBeatmapsFinder:
    def find_beatmaps(self, users):
        "Logic goes here"
        return beatmaps_list


class FilterBeatmapsFinder:
    def find_beatmaps(self, filters):
        "Logic goes here"
        return beatmaps_list
