# nested_bulk_insert

보통 rails에서 ORM으로 bulk-insert를 하기 위해 [activerecord-import](https://github.com/zdennis/activerecord-import)라는 gem을 많이 사용한다. activerecord-import에서는 nested한 bulk insert도 가능하다. 
  
</br>

PostgreSQL만 지원한다. 또, 인자로 일반적인 array나 array of hash는 지원하지 않고 ActiveRecord objects를 인자로 넘겨야 한다. 즉, new나 build 메서드로 initializing한 모델 인스턴스만 인자로 받는다.

</br>

아래와 같이 new로 MeetingProject를 initializing하고 has_many 관계에 있는 meeting_contents를 build하여 nested하게 인스턴스를 생성해준다음 recursive 옵션을 사용하여 nested하게 bulk insert를 한다.

``` ruby
  bulk_arr = []

  Project.where(progress_status: [:before_construction, :under_construction]).each do |project|
    meeting_project = MeetingProject.new(project_id: project.id, meeting_id: meeting.id)
    meeting_project.meeting_contents.build(MeetingContent::_types.values.map {|value| {_type: value}})
    bulk_arr << meeting_project
  end

  MeetingProject.import bulk_arr, recursive: true

```

<img src="https://github.com//Guk0/TIL/blob/master/images/nested_bulk_insert.png?raw=true" alt="drawing" width="600"/>
