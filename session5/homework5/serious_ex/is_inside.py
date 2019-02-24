def is_inside(point,rec):
    if rec[0]<point[0]<rec[0]+rec[2] and rec[2]<point[1]<rec[2]+rec[3]:
        r=True
    else:
        r=False
    print(r)
is_inside([100, 120], [140, 60, 	])