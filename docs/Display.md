# Display


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_scheme** | **str** |  | [optional] 
**low_intensity** | **int** |  | [optional] 
**high_intensity** | **int** |  | [optional] 
**low_load** | **int** |  | [optional] 
**high_load** | **int** |  | [optional] 
**use_paired_workout_color** | **bool** |  | [optional] 
**ignore_workout_colors** | **bool** |  | [optional] 
**show_average_hr** | **bool** |  | [optional] 
**show_normalized_watts** | **bool** |  | [optional] 
**show_load** | **bool** |  | [optional] 
**show_work** | **bool** |  | [optional] 
**show_work_above_ftp** | **bool** |  | [optional] 
**show_weight_lifted** | **bool** |  | [optional] 
**show_average_power** | **bool** |  | [optional] 
**show_rpe** | **bool** |  | [optional] 
**show_feel** | **bool** |  | [optional] 
**show_pace** | **bool** |  | [optional] 
**show_gap** | **bool** |  | [optional] 
**show_intensity** | **bool** |  | [optional] 
**show_name** | **bool** |  | [optional] 
**show_intervals** | **bool** |  | [optional] 
**show_skyline_chart** | **bool** |  | [optional] 
**show_paired_workout_chart** | **bool** |  | [optional] 
**show_description** | **bool** |  | [optional] 
**show_start_time** | **bool** |  | [optional] 
**precise_distance** | **bool** |  | [optional] 
**shrink_warmup** | **bool** |  | [optional] 
**shrink_cooldown** | **bool** |  | [optional] 
**shrink_commute** | **bool** |  | [optional] 
**color** | **str** |  | [optional] 
**color2** | **str** |  | [optional] 

## Example

```python
from intervals_icu_client.models.display import Display

# TODO update the JSON string below
json = "{}"
# create an instance of Display from a JSON string
display_instance = Display.from_json(json)
# print the JSON string representation of the object
print(Display.to_json())

# convert the object into a dict
display_dict = display_instance.to_dict()
# create an instance of Display from a dict
display_from_dict = Display.from_dict(display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


