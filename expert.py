class Expert:
    def __init__(self, screen, persistence):
        self.screen = screen
        self.persistence = persistence
        self.beatmaps_finder_factory = BeatmapsFinderFactory()

    def find_beatmaps(self, inputs):
        beatmap_finder = self.beatmaps_finder_factory.create_beatmap_finder(inputs)
        beatmaps_list = beatmap_finder.find_beatmaps()
        self.beatmaps_list = beatmaps_list
        # downloader = Downloader(bm_list)
