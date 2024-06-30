provider "aws" {
  region = "us-east-1"  # Escolha a região da AWS onde deseja criar a instância EC2
}

# Definição da instância EC2
resource "aws_instance" "scraping_instance" {
  ami                    = "ami-12345678"  # AMI do Amazon Linux 2 (ou outra AMI de sua escolha)
  instance_type          = "t2.micro"      # Tipo da instância EC2
  key_name               = "your-keypair"  # Nome do par de chaves SSH existente na AWS
  security_groups        = ["default"]     # Grupo de segurança (pode ajustar conforme necessário)
  
  tags = {
    Name = "ScrapingInstance"  # Nome da instância EC2
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y python3-pip
              sudo yum install -y wget unzip
              curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
              source $HOME/.poetry/env
              EOF
}

resource "null_resource" "run_scraper" {
  provisioner "remote-exec" {
    inline = [
      "source $HOME/.poetry/env",
      "poetry install",
      "chmod +x scraper.py",
      "python3 scraper.py"
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"  # Usuário padrão do Amazon Linux
      private_key = file("path/to/your/private-key.pem")  # Caminho para sua chave privada SSH
      host        = aws_instance.scraping_instance.public_ip  # IP público da instância EC2
    }
  }
}
