```PlantUML
@startuml
class WeatherReport {
  +GetEvent()
  +ProcessEvent()
  +CreateClassDiagram()
  +ReadStateMachine()
}

WeatherReport -> "Fake Implementation" : Process Event

@enduml
```

```PlantUML

@startuml
[*] --> Idle : Start

state "Idle" as Idle {
  [*] --> Idle : Start
  Idle --> GettingEvent : Get Event
}

state "Getting Event" as GettingEvent {
  GettingEvent --> ProcessingEvent : Event Found
}

state "Processing Event" as ProcessingEvent {
  ProcessingEvent --> CreatingClassDiagram : Event Processed
}

state "Creating Class Diagram" as CreatingClassDiagram {
  CreatingClassDiagram --> ReadingStateMachine : Class Diagram Created
}

state "Reading State Machine" as ReadingStateMachine {
  ReadingStateMachine --> [*] : State Machine Read
}
@enduml
```



![](F:\课程存档\2023春\SoftwareEngineering\work\1.png)



![](F:\课程存档\2023春\SoftwareEngineering\work\2.png)
