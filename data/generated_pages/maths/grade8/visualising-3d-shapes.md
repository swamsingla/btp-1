---
{
  "concept": "Visualising 3D Shapes",
  "slug": "visualising-3d-shapes",
  "grade": 8,
  "language": "en",
  "subject": "maths",
  "area": "Mensuration",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1375,
    "prompt_tokens": 3040,
    "total_tokens": 4415,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    950,
    1300
  ],
  "generated_at": "2026-10-12T21:51:28",
  "source_grade": 8,
  "grade_delta": 0,
  "hand_edited": "2026-10-12: line-by-line hand audit against the textbook, edited directly: removed the Euler's formula section (not in the Grade 8 textbook; it appears only in the Grade 11 and 12 books), replaced with the textbook's prism/pyramid counting questions answered correctly; rewrote the muddled profile examples (a cuboid front view was given as the square outline, cube is the right solid) and the contrasting-profile examples.",
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part2_chapter4_007",
      "chapter": "chapter4",
      "section": "4.2 Visualising Solids"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 4,
    "words": 1020,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 1,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9561
    }
  },
  "terms": [
    "faces",
    "edges",
    "vertices",
    "polyhedra",
    "prism",
    "pyramid",
    "net",
    "euler's formula"
  ]
}
---

# Visualising 3D Shapes

When you look at a solid object, you are really seeing its profile from a specific viewpoint. Depending on your viewpoint, the outline of this profile can vary dramatically. Imagine an elephant passing through a wall; it would leave a hole shaped exactly like its outline. This means that a single solid object can cast very different shadows or profiles depending on the direction you view it from. Understanding these profiles and the basic parts of a solid, such as its faces, edges, and vertices, is the foundation of spatial geometry.

## Profiles of Solids

In previous classes, you have studied solids such as cubes, spheres, cylinders, and cones. Now, you can explore how their profiles change based on the viewpoint. A profile is simply the outline or shadow of a solid when viewed from a particular direction. 

Here are some examples. A cube viewed from the front has a square outline. A sphere has a circular outline from every viewpoint, and a cylinder or a cone viewed from directly above also has a circular outline. A cone or a pyramid viewed from the side has a triangular outline, and so does a triangular prism viewed from its end. 

You can also imagine solids that have contrasting profiles. A cylinder has a rectangular profile from the side and a circular profile from above. A cone has a triangular profile from the side and a circular profile from above. A triangular prism lying on one of its rectangular faces has a rectangular profile from the front and a triangular profile from the end. The key is to visualize the solid passing through a wall, leaving a hole of the appropriate shape. More than one solid can fit the same description.

## Faces, Edges, and Vertices

When discussing solids that contain plane surfaces in their boundaries, the notion of faces, edges, and vertices serves a useful purpose. 

*   **Faces** are the plane or flat surfaces of a solid that form its boundary.
*   **Edges** are the line segments that form the sides of the faces.
*   **Vertices** are the points at which the edges meet.

For example, a cuboid or cube has 6 faces, 12 edges, and 8 vertices.

### Prisms

A prism, in general, has two congruent polygons as opposite faces, with edges connecting the corresponding vertices of these polygons. All the other faces are parallelograms. Based on the shape of the congruent polygons, prisms may be called triangular prisms, pentagonal prisms, and so on.

### Pyramids

A pyramid, in general, has a polygonal base and a point outside it, and edges connect the point with each of the vertices of the base. Based on the shape of the base, pyramids may be called triangular pyramids, square pyramids, pentagonal pyramids, and so on. A triangular pyramid is also known as a tetrahedron.

## Nets of Solids

Many basic solid shapes such as a cuboid, parallelopiped, cylinder, cone, prism, and pyramid can be made using foldable flat materials like paper, cardboard, and even metallic sheets. This is one of the methods for manufacturing hollow solids.

The basic idea is to create a shape on a flat surface that can be folded into the solid. Such a shape is called a net. In other words, a net is obtained by 'unfolding' a solid onto a plane. 

For example, a net of a cube is a flat pattern that can be folded to form a cube. There are multiple possible nets one can use to build a cube. 

When making an actual cube from its net, certain practical aspects have to be kept in mind. One is that the material used must have sufficient sturdiness for the cube to stand. The second aspect is that there should be some mechanism for attaching the faces together. If cardboard or a similar material is used, cello tape is one way to join the adjacent faces. For less sturdy materials, such as chart paper, it is useful to have extra 'flaps' on some of the faces that can be stuck to the adjacent faces. However, when we talk about the net of a solid, we consider only the shape formed by unfolding the solid, and not the other supporting flaps that we may use to actually make the solid.

## Counting Faces, Edges and Vertices

A prism whose two congruent polygons have $n$ sides has $n + 2$ faces (two polygons and $n$ parallelograms), $3n$ edges and $2n$ vertices. A pyramid whose base has $n$ sides has $n + 1$ faces, $2n$ edges and $n + 1$ vertices.

### Worked example

A pentagonal prism has two pentagons as its congruent polygons, so $n = 5$. It has $5 + 2 = 7$ faces, $3 \times 5 = 15$ edges and $2 \times 5 = 10$ vertices.

### Worked example

A square pyramid has a square base, so $n = 4$. It has $4 + 1 = 5$ faces (one square and four triangles), $2 \times 4 = 8$ edges and $4 + 1 = 5$ vertices.

## Key points

*   A solid's profile or shadow can change dramatically depending on the viewpoint.
*   Faces are the flat surfaces of a solid, edges are the line segments that form the sides of the faces, and vertices are the points at which the edges meet.
*   A prism has two congruent polygons as opposite faces, with edges connecting the corresponding vertices of these polygons.
*   A pyramid has a polygonal base and a point outside it, with edges connecting the point to each of the vertices of the base.
*   A net is a flat pattern that can be folded to form a solid.
*   An $n$-sided prism has $n + 2$ faces, $3n$ edges and $2n$ vertices; an $n$-sided pyramid has $n + 1$ faces, $2n$ edges and $n + 1$ vertices.