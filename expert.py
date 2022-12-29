class Expert:
    def __init__(self, screen, persistence):
        # Associations
        self.screen = screen
        self.persistence = persistence
        self.beatmap_finder_factory = BeatmapFinderFactory()

    def find_beatmap(self, inputs):
        # Instance strategy factory, get the beatmap_list to download and call comparation method
        beatmap_finder = self.beatmap_finder_factory.create_beatmap_finder(inputs)
        beatmap_list = beatmap_finder.find_beatmap()
        self.beatmap_list = beatmap_list
        self.compare_beatmap(beatmap_list)

    def compare_beatmap(self, beatmap_list: list[str]):
        # Get local beatmaps and compare with the given list
        self.beatmap_local = self.persistence.beatmap_local
        for i in beatmap_list:
            while i in beatmap_local:
                beatmap_list = beatmap_list.remove(i)

        # Instance and call downloader
        self.downloader = Downloader(self)
        self.downloader.download(beatmap_list)
