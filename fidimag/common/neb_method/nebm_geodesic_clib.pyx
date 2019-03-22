cdef extern from "nebm_geodesic_lib.h":

    double compute_geodesic_GreatCircle(double * A, double * B,
                                        int n_dofs_image,
                                        int * material,
                                        int n_dofs_image_material
                                        )

    double compute_geodesic_Vincenty(double * A, double * B,
                                     int n_dofs_image,
                                     int * material,
                                     int n_dofs_image_material
                                     )

cdef extern from "nebm_lib.h":

    void compute_image_distances(double * distances,
                                 double * path_distances,
                                 double * y,
                                 int n_images,
                                 int n_dofs_image,
                                 double (* compute_distance)(double *,
                                                             double *,
                                                             int,
                                                             int *,
                                                             int),
                                 int *  material,
                                 int n_dofs_image_material
                                 )

def geodesic_distance_Vincenty(double [:] A,
                               double [:] B,
                               n_dofs_image,
                               int [:] material,
                               n_dofs_image_material
                               ):

    return compute_geodesic_Vincenty(&A[0], &B[0], n_dofs_image,
                                    &material[0], n_dofs_image_material
                                    )

def geodesic_distance_GreatCircle(double [:] A,
                                  double [:] B,
                                  n_dofs_image,
                                  int [:] material,
                                  n_dofs_image_material
                                  ):

    return compute_geodesic_GreatCircle(&A[0], &B[0], n_dofs_image,
                                        &material[0], n_dofs_image_material
                                        )


def image_distances_GreatCircle(double [:] distances,
                                double [:] path_distances,
                                double [:] y,
                                int n_images,
                                int n_dofs_image,
                                int [:] material,
                                int n_dofs_image_material
                                ):

    return compute_image_distances(&distances[0],
                                   &path_distances[0],
                                   &y[0],
                                   n_images,
                                   n_dofs_image,
                                   compute_geodesic_GreatCircle,
                                   &material[0],
                                   n_dofs_image_material
                                   )
