import cadquery as cq

part = (
    cq.Workplane("XY")
    .circle(40)
    .extrude(10)
    .faces(">Z")
    .hole(8)
)

part.val().exportStep("part.step")