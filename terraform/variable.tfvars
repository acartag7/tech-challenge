/*
    Sandbox EKS variables
*/
cluster_version          = "1.21"
addon_version_kube_proxy = "v1.21.2-eksbuild.2"
addon_version_coredns    = "v1.8.4-eksbuild.1"
addon_version_vpc_cni    = "v1.9.0-eksbuild.1"
control_plane_logs       = ["api", "audit", "controllerManager", "scheduler"]
private_eks_subnets      = ["10.0.208.0/20", "10.0.224.0/20", "10.0.240.0/20"]

# The cluster was created with 2 nodes and it was not enough to install all the required resources
node_groups = {
  sandbox = {
    min_capacity     = "2"
    desired_capacity = "3"
    max_capacity     = "4"
    instance_types   = ["t3.medium"]
    k8s_labels = {
      k8s-node = "sandbox"
    }
    additional_tags = {
      Env = "sandbox"
    }
  }
}
environment = "sandbox"
