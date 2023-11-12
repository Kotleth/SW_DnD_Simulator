
// pub fn add(left: usize, right: usize) -> usize {
//     left + right
// }
//
// #[cfg(test)]
// mod tests {
//     use super::*;
//
//     #[test]
//     fn it_works() {
//         let result = add(2, 2);
//         assert_eq!(result, 4);
//     }
// }

#[no_mangle]
pub fn testing_function(matrix: &[f32], num_rows: usize) -> (*const f32, usize){
    let a_matrix = make_matrix(matrix, num_rows, num_rows).unwrap();
    let mut temp_vec: Vec<f32> = Vec::new();
    for row in &a_matrix{
        for i in row{
            temp_vec.push(*i);
        }
    }
    let slice_ptr = temp_vec.as_slice().as_ptr();
    let slice_len = temp_vec.len();
    std::mem::forget(temp_vec);
    (slice_ptr, slice_len)
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


