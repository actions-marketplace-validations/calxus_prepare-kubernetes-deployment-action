# Prepare Kubernetes Deployment Action

Action used to prepare the files necessary for a Kubernetes deployment.

## Inputs

### `SERVICE_NAME`

**Required** The name of the service to deploy.

### `SERVICE_REPLICA_COUNT`

**Required** The number of replicas of the service to deploy.

### `SERVICE_IMAGE_NAME`

**Required** The name of the image to deploy.

### `SERVICE_IMAGE_NAMESPACE`

**Required** The namespace of the image to deploy.

### `SERVICE_IMAGE_VERSION`

**Required** The version of the image to deploy.

## Example usage

```
uses: gtadam/prepare-kubernetes-deployment-action@latest
with:
  SERVICE_NAME: 'my-service'
  SERVICE_REPLICA_COUNT: '3'
  SERVICE_IMAGE_NAME: 'my-service'
  SERVICE_IMAGE_NAMESPACE: 'my-namespace'
  SERVICE_IMAGE_VERSION: 'latest'
```