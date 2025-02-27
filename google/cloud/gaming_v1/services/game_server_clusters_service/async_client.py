# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.gaming_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.gaming_v1.services.game_server_clusters_service import pagers
from google.cloud.gaming_v1.types import common, game_server_clusters

from .client import GameServerClustersServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, GameServerClustersServiceTransport
from .transports.grpc_asyncio import GameServerClustersServiceGrpcAsyncIOTransport


class GameServerClustersServiceAsyncClient:
    """The game server cluster maps to Kubernetes clusters running
    Agones and is used to manage fleets within clusters.
    """

    _client: GameServerClustersServiceClient

    DEFAULT_ENDPOINT = GameServerClustersServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = GameServerClustersServiceClient.DEFAULT_MTLS_ENDPOINT

    game_server_cluster_path = staticmethod(
        GameServerClustersServiceClient.game_server_cluster_path
    )
    parse_game_server_cluster_path = staticmethod(
        GameServerClustersServiceClient.parse_game_server_cluster_path
    )
    common_billing_account_path = staticmethod(
        GameServerClustersServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        GameServerClustersServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        GameServerClustersServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        GameServerClustersServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        GameServerClustersServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        GameServerClustersServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        GameServerClustersServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        GameServerClustersServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        GameServerClustersServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        GameServerClustersServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            GameServerClustersServiceAsyncClient: The constructed client.
        """
        return GameServerClustersServiceClient.from_service_account_info.__func__(GameServerClustersServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            GameServerClustersServiceAsyncClient: The constructed client.
        """
        return GameServerClustersServiceClient.from_service_account_file.__func__(GameServerClustersServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return GameServerClustersServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> GameServerClustersServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            GameServerClustersServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(GameServerClustersServiceClient).get_transport_class,
        type(GameServerClustersServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, GameServerClustersServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the game server clusters service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.GameServerClustersServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = GameServerClustersServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_game_server_clusters(
        self,
        request: Optional[
            Union[game_server_clusters.ListGameServerClustersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListGameServerClustersAsyncPager:
        r"""Lists game server clusters in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_list_game_server_clusters():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                request = gaming_v1.ListGameServerClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_game_server_clusters(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.ListGameServerClustersRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.ListGameServerClusters.
            parent (:class:`str`):
                Required. The parent resource name,
                in the following form:
                "projects/{project}/locations/{location}/realms/{realm}".

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1.services.game_server_clusters_service.pagers.ListGameServerClustersAsyncPager:
                Response message for
                GameServerClustersService.ListGameServerClusters.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_clusters.ListGameServerClustersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_game_server_clusters,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListGameServerClustersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.GetGameServerClusterRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_clusters.GameServerCluster:
        r"""Gets details of a single game server cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_get_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                request = gaming_v1.GetGameServerClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_game_server_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.GetGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.GetGameServerCluster.
            name (:class:`str`):
                Required. The name of the game server cluster to
                retrieve, in the following form:
                ``projects/{project}/locations/{location}/realms/{realm-id}/gameServerClusters/{cluster}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1.types.GameServerCluster:
                A game server cluster resource.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_clusters.GetGameServerClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_game_server_cluster,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.CreateGameServerClusterRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        game_server_cluster: Optional[game_server_clusters.GameServerCluster] = None,
        game_server_cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new game server cluster in a given project
        and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_create_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                game_server_cluster = gaming_v1.GameServerCluster()
                game_server_cluster.name = "name_value"

                request = gaming_v1.CreateGameServerClusterRequest(
                    parent="parent_value",
                    game_server_cluster_id="game_server_cluster_id_value",
                    game_server_cluster=game_server_cluster,
                )

                # Make the request
                operation = client.create_game_server_cluster(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.CreateGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.CreateGameServerCluster.
            parent (:class:`str`):
                Required. The parent resource name, in the following
                form:
                ``projects/{project}/locations/{location}/realms/{realm-id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            game_server_cluster (:class:`google.cloud.gaming_v1.types.GameServerCluster`):
                Required. The game server cluster
                resource to be created.

                This corresponds to the ``game_server_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            game_server_cluster_id (:class:`str`):
                Required. The ID of the game server
                cluster resource to be created.

                This corresponds to the ``game_server_cluster_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gaming_v1.types.GameServerCluster`
                A game server cluster resource.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any(
            [parent, game_server_cluster, game_server_cluster_id]
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_clusters.CreateGameServerClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if game_server_cluster is not None:
            request.game_server_cluster = game_server_cluster
        if game_server_cluster_id is not None:
            request.game_server_cluster_id = game_server_cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_game_server_cluster,
            default_timeout=120.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            game_server_clusters.GameServerCluster,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def preview_create_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.PreviewCreateGameServerClusterRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_clusters.PreviewCreateGameServerClusterResponse:
        r"""Previews creation of a new game server cluster in a
        given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_preview_create_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                game_server_cluster = gaming_v1.GameServerCluster()
                game_server_cluster.name = "name_value"

                request = gaming_v1.PreviewCreateGameServerClusterRequest(
                    parent="parent_value",
                    game_server_cluster_id="game_server_cluster_id_value",
                    game_server_cluster=game_server_cluster,
                )

                # Make the request
                response = await client.preview_create_game_server_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.PreviewCreateGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.PreviewCreateGameServerCluster.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1.types.PreviewCreateGameServerClusterResponse:
                Response message for
                GameServerClustersService.PreviewCreateGameServerCluster.

        """
        # Create or coerce a protobuf request object.
        request = game_server_clusters.PreviewCreateGameServerClusterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.preview_create_game_server_cluster,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.DeleteGameServerClusterRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single game server cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_delete_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                request = gaming_v1.DeleteGameServerClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_game_server_cluster(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.DeleteGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.DeleteGameServerCluster.
            name (:class:`str`):
                Required. The name of the game server cluster to delete,
                in the following form:
                ``projects/{project}/locations/{location}/gameServerClusters/{cluster}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_clusters.DeleteGameServerClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_game_server_cluster,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def preview_delete_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.PreviewDeleteGameServerClusterRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_clusters.PreviewDeleteGameServerClusterResponse:
        r"""Previews deletion of a single game server cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_preview_delete_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                request = gaming_v1.PreviewDeleteGameServerClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.preview_delete_game_server_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.PreviewDeleteGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.PreviewDeleteGameServerCluster.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1.types.PreviewDeleteGameServerClusterResponse:
                Response message for
                GameServerClustersService.PreviewDeleteGameServerCluster.

        """
        # Create or coerce a protobuf request object.
        request = game_server_clusters.PreviewDeleteGameServerClusterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.preview_delete_game_server_cluster,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.UpdateGameServerClusterRequest, dict]
        ] = None,
        *,
        game_server_cluster: Optional[game_server_clusters.GameServerCluster] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Patches a single game server cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_update_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                game_server_cluster = gaming_v1.GameServerCluster()
                game_server_cluster.name = "name_value"

                request = gaming_v1.UpdateGameServerClusterRequest(
                    game_server_cluster=game_server_cluster,
                )

                # Make the request
                operation = client.update_game_server_cluster(request=request)

                print("Waiting for operation to complete...")

                response = (await operation).result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.UpdateGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.UpdateGameServerCluster.
            game_server_cluster (:class:`google.cloud.gaming_v1.types.GameServerCluster`):
                Required. The game server cluster to be updated. Only
                fields specified in update_mask are updated.

                This corresponds to the ``game_server_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. For the ``FieldMask``
                definition, see
                https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gaming_v1.types.GameServerCluster`
                A game server cluster resource.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([game_server_cluster, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_clusters.UpdateGameServerClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if game_server_cluster is not None:
            request.game_server_cluster = game_server_cluster
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_game_server_cluster,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("game_server_cluster.name", request.game_server_cluster.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            game_server_clusters.GameServerCluster,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def preview_update_game_server_cluster(
        self,
        request: Optional[
            Union[game_server_clusters.PreviewUpdateGameServerClusterRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_clusters.PreviewUpdateGameServerClusterResponse:
        r"""Previews updating a GameServerCluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gaming_v1

            async def sample_preview_update_game_server_cluster():
                # Create a client
                client = gaming_v1.GameServerClustersServiceAsyncClient()

                # Initialize request argument(s)
                game_server_cluster = gaming_v1.GameServerCluster()
                game_server_cluster.name = "name_value"

                request = gaming_v1.PreviewUpdateGameServerClusterRequest(
                    game_server_cluster=game_server_cluster,
                )

                # Make the request
                response = await client.preview_update_game_server_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gaming_v1.types.PreviewUpdateGameServerClusterRequest, dict]]):
                The request object. Request message for
                GameServerClustersService.UpdateGameServerCluster.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1.types.PreviewUpdateGameServerClusterResponse:
                Response message for
                GameServerClustersService.PreviewUpdateGameServerCluster

        """
        # Create or coerce a protobuf request object.
        request = game_server_clusters.PreviewUpdateGameServerClusterRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.preview_update_game_server_cluster,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("game_server_cluster.name", request.game_server_cluster.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "GameServerClustersServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("GameServerClustersServiceAsyncClient",)
