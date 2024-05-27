from itertools import groupby
from operator import itemgetter
from django.db.models.fields import DateTimeField
from django.db.models.functions import Trunc
from Production.models import ProductionLinePerformance, StorageData, CharacteristicProductionLine


def get_performance_production_lines():
    data = []
    for id in [1, 2, 3]:
        # lines = list(ProductionLinePerformance.objects.filter(production_line__id=id)
        #             .values('production_line', 'timestamp', 'performance')
        #             .order_by('-timestamp')[:10])
        # data.extend(lines)
        lines = list(ProductionLinePerformance.objects.filter(production_line__id=id)
            .annotate(timestamp_truncated=Trunc('timestamp', 'minute', output_field=DateTimeField()))
            .values('production_line', 'timestamp_truncated', 'performance')
            .order_by('-timestamp_truncated')[:10])
        data.extend(lines)
        
    # grouped_data = {}
    # for perf in data:
    #     timestamp = perf["timestamp"].strftime("%Y-%m-%dT%H:%M:%S.%f")
    #     if timestamp not in grouped_data:
    # # grouped_data[timestamp] = {"storage": data["storage"], "performance": []}
    #         grouped_data[timestamp].append({"production_line": perf["production_line"], "performance": perf["performance"]})

    data.sort(key=itemgetter("timestamp_truncated"))
    # Группировка по timestamp
    result = []
    for key, group in groupby(data, key=itemgetter("timestamp_truncated")):
        group_list = list(group)
        result.append({
        "production_line": [x["production_line"] for x in group_list],
        "timestamp": key,
        "performance": [x["performance"] for x in group_list]
        })
                                    
    return result

def get_storage_data():
    data = list(StorageData.objects.all().values('name', 'count'))
    return data
    
    
def get_characteristic_production_lines():
    data = list(CharacteristicProductionLine.objects.all().values('production_line__name', 'efficiency', 'operational_hours', 'maintenance_frequency', 'energy_consumption', 'staff_required', 'downtime_per_month'))
    return data