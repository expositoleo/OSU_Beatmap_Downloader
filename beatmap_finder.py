from abc import ABC, abstractmethod


class BeatmapFinderFactory:
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


class BeatmapFinder(ABC):
    @abstractmethod
    def find_beatmap(self, data):
        pass


"""
STRATEGY CLASS TEMPLATE:

class ?BeatmapFinder:
    def find_beatmap(self, data):
        "Logic goes here"
        return beatmap_list

"""


class UserBeatmapFinder:
    def find_beatmap(self, users):
        "Logic goes here"
        return beatmap_list


class FilterBeatmapFinder:
    def find_beatmap(self, filters):
        "Logic goes here"
        return beatmap_list
