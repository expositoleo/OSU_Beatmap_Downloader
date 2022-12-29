```mermaid
classDiagram
    %% Beatmap is also called beatmap for legibility
    BeatmapFinder <|-- ByUser
    BeatmapFinder <|-- ByFilter
    BeatmapFinderFactory <-- Expert : input
    ByFilter <-- BeatmapFinderFactory : input
    ByUser <-- BeatmapFinderFactory : input
    Expert <-- Screen : input
    Expert <-- Persistence : db_list
    Downloader <-- Expert : beatmap_list
    Expert <-- BeatmapFinder : beatmap_list
    Persistence <-- Screen : data_path

    class BeatmapFinder{
        +beatmap_list : List~int~
        find_beatmap()* List~int~
    }
    class ByUser{
        -find_beatmap(input)
    }
    class ByFilter{
        -find_beatmap(input)
    }
    class Screen{
        <<Interface>>
        +inputs()
    }
    class Persistence{
        +local_list : List~int~
        -update() List~int~
    }
    class Downloader{
        +status : Dict
        -download(List~int~) Dict~Bool~
    }
    class Expert{
        <<Abstract>>
        +beatmap_list : List~int~
        +input : Any
        -compare_beatmap(List~int~)
    }
    class BeatmapFinderFactory{
        +input : Any
    }

```
