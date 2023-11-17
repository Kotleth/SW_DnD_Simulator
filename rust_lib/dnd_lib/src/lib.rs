use std::collections::{BinaryHeap, HashMap, HashSet};
use std::cmp::Ordering;

#[derive(Eq, PartialEq)]
struct Node {
    name: (usize, usize),
    distance: u32,
}

impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        other.distance.cmp(&self.distance)
    }
}

impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

#[no_mangle]
pub fn dijkstra(in_matrix: &[f32], rows: usize, x_start: usize, y_start: usize) -> (*const i32, usize)
{
    let init_matrix: Vec<u32> = in_matrix.clone().iter().map(|&x| x as u32).collect();
    let start: (usize, usize) = (x_start, y_start);
    let mut init_graph: HashMap<(usize, usize), HashMap<(usize, usize), u32>> = HashMap::new();
    let cols: usize = init_matrix.len() / rows;
    for i in 0..init_matrix.len() {
        init_graph.insert((i % rows, (i - i % rows) / rows), HashMap::new());
        for j in [-1, 1] {
            // These are for top and bottom boundaries
            if ((i % rows != 0) | (j == 1)) & ((i % rows != rows - 1) | (j == -1)) {
                let neighbour_row: usize = ((i % rows) as i32 + j) as usize;
                init_graph.get_mut(&(i % rows, (i - i % rows) / rows)).map(|val| val.insert((neighbour_row, (i - i % rows) / rows), init_matrix[(i as i32 + j) as usize]));
            }
            // These are for left and right boundaries
            if (((i - i % rows) / rows != 0) | (j == 1)) & (((i - i % rows) / rows != cols - 1) | (j == -1)) {
                let neighbour_col: usize = (((i - i % rows) / rows) as i32 + j) as usize;
                init_graph.get_mut(&(i % rows, (i - i % rows) / rows)).map(|val| val.insert((i % rows, neighbour_col), init_matrix[(i as i32 + j * rows as i32) as usize]));
            }
        }
    }
    let graph = init_graph.clone();
    let mut distances: HashMap<(usize, usize), u32> = init_graph.keys().map(|&k| (k, u32::MAX)).collect();
    let mut priority_queue = BinaryHeap::new();
    let mut visited: HashSet<(usize, usize)> = HashSet::new();

    distances.insert(start, 0);
    priority_queue.push(Node { name: start, distance: 0 });
    while let Some(Node { name, distance }) = priority_queue.pop() {
        if visited.contains(&name) {
            continue;
        }

        visited.insert(name);

        for (&neighbor, &weight) in graph[&name].iter() {
            let new_distance = distance + weight;
            if new_distance < *distances.get(&neighbor).unwrap() {
                distances.insert(neighbor, new_distance);
                priority_queue.push(Node { name: neighbor, distance: new_distance });
            }
        }
    }

    let mut temp_keys_vec = Vec::new();
    let mut temp_values_vec = Vec::new();

    // Make it a pointer to pass it to python
    for (&keys, &values) in distances.iter() {
        let (x, y) = keys;
        temp_keys_vec.push(x as i32);
        temp_keys_vec.push(y as i32);
        temp_values_vec.push(values as i32);
    }
    temp_keys_vec.append(&mut temp_values_vec);
    let merged_vec = temp_keys_vec;

    let slice_pointer = merged_vec.as_slice().as_ptr();
    let slice_len = merged_vec.len();
    std::mem::forget(merged_vec);
    (slice_pointer, slice_len)
}

fn make_matrix(vector: &[f32], num_rows: usize, num_columns: usize) -> Result<Vec<Vec<f32>>, String> {
    let mut res_mat: Vec<Vec<f32>> = Vec::new();
    if vector.len()%num_rows != 0 {
            return Err(String::from("Matrix rows does not match data length."));
    } else if (vector.len()/num_rows)%num_columns != 0 {
            return Err(String::from("Matrix columns does not match data length."));
    } else {
        for i in 0..num_rows {
            res_mat.push(Vec::new());
            for j in 0..num_columns {
                res_mat[i].push(vector[i * num_rows + j]);
            }
        }
        Ok(res_mat)
    }
}

