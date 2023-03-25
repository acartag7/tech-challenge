# create a repository in ECR

resource "aws_ecr_repository" "tech_challenge" {
  name                 = "tech_challenge_arnold"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

output "ecr_repository_name" {
  value = aws_ecr_repository.tech_challenge.name
}
